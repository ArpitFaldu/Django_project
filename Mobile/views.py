from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from firstapp.models import Device,Wishlist
from django.contrib.auth.models import User
def mobile(request):
    # Initial queryset with all devices
    devices = Device.objects.filter(Type="Mobile").order_by("-device_id")

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

    # Render the template with the filtered queryset
    return render(request, 'mobile.html', {'device': devices})

def add_to_wishlist(request):
    if request.method == 'POST':
        device_id_str = request.POST.get('device_id')
        if device_id_str is not None:
            print(device_id_str)
        if device_id_str:
            try:
                device_id = int(device_id_str)
                # Assuming you have a logged-in user, you can get the user from request.user
                user = request.user
                device = Device.objects.get(pk=device_id)
                if Wishlist.objects.filter(user_id=user, device_id=device).exists():
                    return HttpResponse("Device already exists in wishlist.")
                Wishlist.objects.create(user_id=user, device_id=device)
                return HttpResponse("Device added to wishlist successfully!")
            except ValueError:
                return HttpResponse("Invalid device ID provided.")
            except Device.DoesNotExist:
                return HttpResponse("Device does not exist.")
        else:
            return HttpResponse("Device ID not provided.")
    else:
        return HttpResponse("Only POST requests are allowed.")
    
def wishlist(request):
    user_id = request.user.id
    return render(request,"wishlist.html",{'wishlist':Wishlist.objects.all(),'user_id':user_id})

def remove_from_wishlist(request,wishlist_id):
    if request.method == 'POST':
        # Assuming you have a logged-in user, you can get the user from request.user
        user = request.user
        # Retrieve the wishlist item by its ID and user
        wishlist_item = get_object_or_404(Wishlist, pk=wishlist_id, user_id=user)

        # Delete the wishlist item
        wishlist_item.delete()
        return HttpResponse("Item removed from wishlist successfully!")        
    else:
        return HttpResponse("Only POST requests are allowed.")



def comparemobile(request):
    if request.method == 'POST':
        devices = Device.objects.filter(Type="Mobile")
        device1_name = request.POST.get('device1_name')
        device2_name = request.POST.get('device2_name')
       
        try:
            print("hi")
            device1 = Device.objects.get(name=device1_name)
            device2 = Device.objects.get(name=device2_name)
            print(device1)
        except Device.DoesNotExist:
            #  one or both devices do not exist
            device1 = None
            device2 = None
       
        return render(request, 'compare_result.html', {'device1': device1, 'device2': device2})
    else:
        # request method is not POST
        return render(request, 'mobile.html')
