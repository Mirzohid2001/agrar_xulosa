import os
from django.db.models import Sum
from openpyxl import Workbook
from .models import Region, WorkType, Seed, Fertiliser, News, Review, Banner, Statistic, Legal_Documents
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
import xlsxwriter
from .serializers import NewsSerializer, ReviewSerializer, BannerSerializer, Legal_DocumentsSerializer
import os
import xlsxwriter
from django.db.models import Sum
from django.http import HttpResponse, FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Region, Tractor, Worker, WorkType, Seed, Fertiliser, Order
import os
import time
import random
from django.conf import settings


class DetailedCostBreakdownAPIView(APIView):
    def get(self, request):
        try:
            regions = Region.objects.all().values_list('name', flat=True)
            work_types = WorkType.objects.all().values_list('name', flat=True)
            seeds = Seed.objects.all().values_list('name', flat=True)
            fertilisers = Fertiliser.objects.all().values_list('name', flat=True)

            return Response({
                "regions": list(regions),
                "work_types": list(work_types),
                "seeds": list(seeds),
                "fertilisers": list(fertilisers),
            })
        except Exception as e:
            return Response({"error": str(e)}, status=400)

    def post(self, request):
        try:
            region_name = request.data.get('region')
            area_str = request.data.get('area')
            work_type_name = request.data.get('work_type')
            seed_name = request.data.get('seed')
            fertiliser_name = request.data.get('fertiliser')
            tractor_count = request.data.get('tractor_count')
            workers_count = request.data.get('workers_count')
            seed_quantity_per_hectare = request.data.get('seed_quantity_per_hectare')
            fertiliser_quantity_per_hectare = request.data.get('fertiliser_quantity_per_hectare')
            fuel_consumption_per_hectare = request.data.get('fuel_consumption_per_hectare')

            if not all([region_name, area_str, work_type_name, seed_name, fertiliser_name,
                        tractor_count, workers_count, seed_quantity_per_hectare,
                        fertiliser_quantity_per_hectare, fuel_consumption_per_hectare]):
                return Response({"error": "Пожалуйста, предоставьте все необходимые данные."}, status=400)

            area = float(area_str)
            tractor_count = int(tractor_count)
            workers_count = int(workers_count)
            seed_quantity_per_hectare = float(seed_quantity_per_hectare)
            fertiliser_quantity_per_hectare = float(fertiliser_quantity_per_hectare)
            fuel_consumption_per_hectare = float(fuel_consumption_per_hectare)

            region = Region.objects.get(name=region_name)
            work_type = WorkType.objects.get(place=region, name=work_type_name)
            seed = Seed.objects.get(place=region, name=seed_name)
            fertiliser = Fertiliser.objects.get(place=region, name=fertiliser_name)

            worker_cost = workers_count * work_type.worker.salary
            tractor_cost_per_hectare = tractor_count * work_type.tractor.price_a_hectare
            seed_cost_per_hectare = seed_quantity_per_hectare * seed.price
            fertiliser_cost_per_hectare = fertiliser_quantity_per_hectare * fertiliser.price
            fuel_cost_per_hectare = fuel_consumption_per_hectare * work_type.tractor.price_a_moto
            total_cost_per_hectare = worker_cost + tractor_cost_per_hectare + seed_cost_per_hectare + fertiliser_cost_per_hectare + fuel_cost_per_hectare

            total_cost_for_area = total_cost_per_hectare * area

            excel_folder = os.path.join(settings.MEDIA_ROOT, "excel_files")
            if not os.path.exists(excel_folder):
                os.makedirs(excel_folder)

            timestamp = str(int(time.time()))
            random_number = str(random.randint(1000, 9999))
            excel_file_name = f"detailed_cost_breakdown_{timestamp}_{random_number}.xlsx"
            excel_file_path = os.path.join(excel_folder, excel_file_name)
            workbook = xlsxwriter.Workbook(excel_file_path)
            worksheet = workbook.add_worksheet("Detailed Cost Breakdown")
            header_format = workbook.add_format(
                {'bold': True, 'align': 'center', 'valign': 'vcenter', 'text_wrap': True, 'border': 1})
            data_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'text_wrap': True, 'border': 1})
            worksheet.write(0, 0, "Категория", header_format)
            worksheet.write(0, 1, "Стоимость за гектар", header_format)
            worksheet.write(0, 2, "Общая стоимость для указанной площади", header_format)
            worksheet.write(0, 3, "Общая стоимость", header_format)
            additional_costs = {
                "Стоимость рабочего": worker_cost,
                "Стоимость трактора": tractor_cost_per_hectare,
                "Стоимость семян": seed_cost_per_hectare,
                "Стоимость удобрений": fertiliser_cost_per_hectare,
                "Стоимость топлива": fuel_cost_per_hectare,
            }

            row = 1
            total_cost_all_positions = 0
            for category, cost in additional_costs.items():
                worksheet.write(row, 0, category, data_format)
                worksheet.write_number(row, 1, cost, data_format)
                worksheet.write_number(row, 2, cost * area, data_format)
                worksheet.write_number(row, 3, cost * area, data_format)
                total_cost_all_positions += cost * area
                row += 1
            worksheet.write(row, 0, "Общая стоимость по всем позициям", header_format)
            worksheet.write_number(row, 3, total_cost_all_positions, data_format)

            workbook.close()

            # Генерация ссылки для скачивания файла
            file_url = f"https://ustomirzohidn1.pythonanywhere.com/home/UstoMirzohidN1/agrar_xulosa/media/excel_files/{excel_file_name}"

            return Response({"excel_file_url": file_url})

        except (Region.DoesNotExist, WorkType.DoesNotExist, Seed.DoesNotExist, Fertiliser.DoesNotExist):
            return Response({"error": "Один или несколько элементов не найдены."}, status=400)
        except ValueError:
            return Response({"error": "Предоставлены неверные данные."}, status=400)


class NewsAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ReviewAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BannerAPIView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class Legal_DocumentsAPIView(generics.ListAPIView):
    queryset = Legal_Documents.objects.all()
    serializer_class = Legal_DocumentsSerializer


class UserCountAPIView(APIView):
    def get(self, request, format=None):
        from backend.users.models import User
        total_users = User.objects.count()
        if request.user.is_authenticated:
            try:
                statistic = Statistic.objects.get(user=request.user)
            except Statistic.DoesNotExist:
                statistic = Statistic(user=request.user, count=1)
                statistic.save()
            else:
                statistic.count += 1
                statistic.save()
        registered_users_count = Statistic.objects.aggregate(total_registered_users=Sum('count'))[
            'total_registered_users']

        return Response({
            'total_users': total_users
        })
