# from django.shortcuts import render

# # Create your views here.
# from .models import myapp_collection
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("<h1>app is running</h1>")

# storing hardcoded data in database 

# def add_person(request):
#     records={
#         "first_name":"a",
#         "last_name":"j"
#     }
#     myapp_collection.insert_one(records)
#     return HttpResponse("new person added")

# def get_all_persons(request):
#     persons=myapp_collection.find()
#     return HttpResponse(persons)

from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from .models import myapp_collection
from django.views.decorators.csrf import csrf_exempt
import json
import os


def index(request):
    return HttpResponse("<h1>app is running</h1>")

# ------------------------------------------------------------------------------

# creating api to store the data in database statically

# @csrf_exempt
# @require_http_methods(["POST"])
# def add_person(request):
#     if request.method == "POST":
#         records = {
#             "first_name": request.POST.get("first_name", "a"),
#             "last_name": request.POST.get("last_name", "j")
#         }
#         myapp_collection.insert_one(records)
#         return HttpResponse("New person added")
#     else:
#         return HttpResponse("Method not allowed", status=405)
# -------------------------------------------------------------------------------------

# storing fisrtname an lastname in database throug postman body 

# @csrf_exempt
# @require_http_methods(["POST"])
# def add_person(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")

#         if not first_name or not last_name:
#             return HttpResponse("First name and last name are required", status=400)

#         records = {
#             "first_name": first_name,
#             "last_name": last_name
#         }
#         myapp_collection.insert_one(records)
#         return HttpResponse("New person added", status=201)
#     else:
#         return HttpResponse("Method not allowed", status=405)

# =====================================================================================================

# storing name and image in database through postman

import gridfs
import tempfile
from pymongo import MongoClient
from PIL import Image
import base64



client = MongoClient('mongodb+srv://akhila:y4fEYNAFy2mUAa1i@cluster0.4uqtf1s.mongodb.net/')
db = client['newdb']
myapp_collection = db['collection']
# fs = gridfs.GridFS(db)


# @csrf_exempt
# @require_http_methods(["POST"])
# def add_person(request):
#     try:
#         data = json.loads(request.body)
#         first_name = data.get("first_name")
#         last_name = data.get("last_name")
#         image_path = data.get("image_file")

#         if not first_name or not last_name:
#             return JsonResponse({"error": "First name and last name are required"}, status=400)

#         if not image_path or not os.path.isfile(image_path):
#             return JsonResponse({"error": "A valid image file path is required"}, status=400)

#         # Open and read the image from the given path
#         with open(image_path, 'rb') as image_file:
#             image_data = image_file.read()

#         # Encode the image data as a base64 string
#         image_base64 = base64.b64encode(image_data).decode('utf-8')

#         # Create record
#         records = {
#             "first_name": first_name,
#             "last_name": last_name,
#             "image_data": image_base64,
#             "image_name": os.path.basename(image_path)
#         }
#         myapp_collection.insert_one(records)

#         return JsonResponse({"message": "New person added"}, status=201)
#     except json.JSONDecodeError:
#         return JsonResponse({"error": "Invalid JSON body"}, status=400)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)

# ===================================================================================================

# image is storing in database with with image id

# @csrf_exempt
# @require_http_methods(["POST"])
# def add_person(request):
#     try:
#         data = json.loads(request.body)
#         first_name = data.get("first_name")
#         last_name = data.get("last_name")
#         image_path = data.get("image_file")

#         if not first_name or not last_name:
#             return JsonResponse({"error": "First name and last name are required"}, status=400)

#         if not image_path or not os.path.isfile(image_path):
#             return JsonResponse({"error": "A valid image file path is required"}, status=400)

#         # Open and read the image from the given path
#         with open(image_path, 'rb') as image_file:
#             image_data = image_file.read()

#         # Save image to GridFS
#         # image_id = fs.put(image_data, filename=os.path.basename(image_path))
#         image_id = fs.put(image_data, filename=os.path.basename(image_path))


#         # Create record
#         records = {
#             "first_name": first_name,
#             "last_name": last_name,
#             "image_id": image_id
#         }
#         myapp_collection.insert_one(records)

#         return JsonResponse({"message": "New person added"}, status=201)
#     except json.JSONDecodeError:
#         return JsonResponse({"error": "Invalid JSON body"}, status=400)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)
#  ========================================================================================================
# @csrf_exempt
# @require_http_methods(["POST"])
# def add_person(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         image_file = request.FILES.get("image_file")

#         if not first_name or not last_name:
#             return HttpResponse("First name and last name are required", status=400)

#         if not image_file:
#             return HttpResponse("Image file is required", status=400)

#         # Save image to GridFS
#         with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#             for chunk in image_file.chunks():
#                 temp_file.write(chunk)
#             temp_file_path = temp_file.name

#         with open(temp_file_path, 'rb') as f:
#             image_id = fs.put(f, filename=image_file.name)

#         # Create record
#         records = {
#             "first_name": first_name,
#             "last_name": last_name,
#             "image_id": image_id
#         }
#         myapp_collection.insert_one(records)

#         return HttpResponse("New person added", status=201)
#     else:
#         return HttpResponse("Method not allowed", status=405)

# @require_http_methods(["GET"])
# def get_all_persons(request):
#     if request.method == "GET":
#         persons = list(myapp_collection.find())
#         persons_list = [{"first_name": person["first_name"], "last_name": person["last_name"]} for person in persons]
#         return JsonResponse(persons_list, safe=False)
#     else:
#         return HttpResponse("Method not allowed", status=405)




# @require_http_methods(["GET"])
# def get_all_persons(request):
#     try:
#         persons = list(myapp_collection.find({}, {"_id": 0}))  # Exclude the MongoDB '_id' field
#         persons_list = [{
#             "first_name": person.get("first_name", "N/A"),
#             "last_name": person.get("last_name", "N/A"),
#             "image_data": person.get("image_data", ""),  # Include image data if present
#             "image_name": person.get("image_name", "")  # Include image name if present
#         } for person in persons]
#         return JsonResponse(persons_list, safe=False, status=200)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)

# ======================================================================================================================


# import json
# import os
# import base64
# from PIL import Image
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
# from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient('your_mongodb_uri')
# db = client['your_database_name']
# myapp_collection = db['your_collection_name']

@csrf_exempt
@require_http_methods(["POST"])
def add_item(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        quantity = data.get("quantity")
        price = data.get("price")
        image_path = data.get("image_file")

        if not name or quantity is None or price is None:
            return JsonResponse({"error": "Name, quantity, and price are required"}, status=400)

        if not image_path or not os.path.isfile(image_path):
            return JsonResponse({"error": "A valid image file path is required"}, status=400)

        # Open and read the image from the given path
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Encode the image data as a base64 string
        image_base64 = base64.b64encode(image_data).decode('utf-8')

        # Create record
        records = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "image_data": image_base64,
            "image_name": os.path.basename(image_path)
        }
        myapp_collection.insert_one(records)

        return JsonResponse({"message": "New item added"}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



@require_http_methods(["GET"])
def get_all_items(request):
    try:
        items = list(myapp_collection.find({}, {"_id": 0}))  # Exclude the MongoDB '_id' field
        items_list = [{
            "name": item.get("name", "N/A"),
            "quantity": item.get("quantity", 0),
            "price": item.get("price", 0.0),
            "image_data": item.get("image_data", ""),  # Include image data if present
            "image_name": item.get("image_name", "")  # Include image name if present
        } for item in items]
        return JsonResponse(items_list, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)