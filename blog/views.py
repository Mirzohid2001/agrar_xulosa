
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Region, Tractor, Worker, WorkType, Seed, Fertiliser,News
from rest_framework import generics
from .serializers import NewsSerializer


class CostBreakdownAPIView(APIView):
    def post(self, request):
        region_name = request.data.get('region')
        area = float(request.data.get('area'))
        work_type_name = request.data.get('work_type')

        if not all([region_name, area, work_type_name]):
            return Response({"error": "Не все данные были предоставлены."}, status=400)
        try:
            region = Region.objects.get(name=region_name)
        except Region.DoesNotExist:
            return Response({"error": f"Регион '{region_name}' не найден."}, status=400)
        try:
            work_type = WorkType.objects.get(place=region, name=work_type_name)
        except WorkType.DoesNotExist:
            return Response({"error": f"Тип работы '{work_type_name}' для региона '{region_name}' не найден."}, status=400)
        tractor_price = work_type.tractor.price_a_hectare
        worker_salary = work_type.worker.salary
        seed_price = Seed.objects.filter(place=region).first().price if Seed.objects.filter(place=region).exists() else 0
        fertiliser_price = Fertiliser.objects.filter(place=region).first().price if Fertiliser.objects.filter(place=region).exists() else 0
        worker_cost = worker_salary
        tractor_cost = tractor_price * area
        seed_cost = seed_price * area
        fertiliser_cost = fertiliser_price * area
        total_cost = worker_cost + tractor_cost + seed_cost + fertiliser_cost

        return Response({
            "worker_cost": worker_cost,
            "tractor_cost": tractor_cost,
            "seed_cost": seed_cost,
            "fertiliser_cost": fertiliser_cost,
            "total_cost": total_cost
        })



class NewsAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer










