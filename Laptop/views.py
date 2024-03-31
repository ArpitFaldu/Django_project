from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from firstapp.models import Mobile,Laptop,Device, Wishlist

# Create your views here.
def laptop(request):
        # Initial queryset with all devices
    devices = Device.objects.filter(Type="Laptop").order_by("-device_id")

    # List of fields to filter on
    filter_fields = ['name', 'price', 'RAM', 'Storage', 'Battery', 'manufacturer', 'processor', 'screen_height', 'screen_width']

    # Check if any of the filter fields are present in request.POST
    filters = {}
    for field in filter_fields:
        if field in request.POST and request.POST[field].strip():  # Check if value is not empty
            value = request.POST[field]
            # Special case for RAM field
            if field == 'RAM':
                filters[field] = value
                print(filters[field])
            elif field == 'name':
                filters[field + '__contains'] = value
            elif field == 'price':
                filters[field + '__lte'] = value
            elif field == 'Storage':
                filters[field] = value
            # elif field == 'Battery':
            #     # Extract numeric part and convert to integer
            #     value_numeric = value.replace('mAh', '').strip()
            #     print("Hello")
            #     filters[field + '__lte'] = int(value_numeric)
            #     print(filters[field])
            #     print(int(value_numeric))
            elif field == 'Battery':
                val=int(value[:4])
                filters[field+ '__gte'] = val
                filters[field+ '__lte'] = val+500
            elif field == 'manufacturer':
                filters[field] = value
            elif field == 'processor':
                filters[field] = value
            elif field == 'screen_height':
                filters[field + '__gte'] = float(value)
                filters[field + '__lte'] = float(value)+0.5
            elif field == 'screen_width':
                filters[field + '__gte'] = float(value)
                filters[field + '__lte'] = float(value)+0.5
            else:
                # Add filter criterion to the dictionary
                filters[field] = value

    # Apply filters to the queryset
    devices = devices.filter(**filters)

    return render(request,'laptop.html',{'device':devices})
