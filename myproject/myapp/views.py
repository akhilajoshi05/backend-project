
    # according to frontend schema

import json
import os
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://akhila:y4fEYNAFy2mUAa1i@cluster0.4uqtf1s.mongodb.net/')
db = client['newdb']
myapp_collection = db['product']

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
        base64_image = base64.b64encode(image_data).decode('utf-8')

        # Create record
        record = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "image": os.path.basename(image_path),  # This can be the image file name
            "base64Image": base64_image
        }
        myapp_collection.insert_one(record)

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
            "image": item.get("image", ""),  # File name of the image
            "base64Image": item.get("base64Image", "")  # Base64-encoded image data
        } for item in items]
        return JsonResponse(items_list, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PUT"])
def update_item(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")
        quantity = data.get("quantity")
        price = data.get("price")
        image_path = data.get("image_file")

        if not name:
            return JsonResponse({"error": "Name is required"}, status=400)

        updates = {}
        if quantity is not None:
            updates["quantity"] = quantity
        if price is not None:
            updates["price"] = price
        if image_path:
            if not os.path.isfile(image_path):
                return JsonResponse({"error": "A valid image file path is required"}, status=400)
            # Open and read the image from the given path
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
            # Encode the image data as a base64 string
            base64_image = base64.b64encode(image_data).decode('utf-8')
            updates["base64Image"] = base64_image
            updates["image"] = os.path.basename(image_path)

        result = myapp_collection.update_one({"name": name}, {"$set": updates})

        if result.matched_count == 0:
            return JsonResponse({"error": "Item not found"}, status=404)

        return JsonResponse({"message": "Item updated"}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request):
    try:
        data = json.loads(request.body)
        name = data.get("name")

        if not name:
            return JsonResponse({"error": "Name is required"}, status=400)

        result = myapp_collection.delete_one({"name": name})

        if result.deleted_count == 0:
            return JsonResponse({"error": "Item not found"}, status=404)

        return JsonResponse({"message": "Item deleted"}, status=200)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
