import uuid
import asyncio

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from scripts import imitation_send_query



processing_resultats = {}
router = APIRouter()

@router.post('/processing', status_code=202)
async def start_processing(content=Body(default={})):
    cadastral_number = content.get('cadastral_number')
    latitude = content.get('latitude')
    longitude = content.get('longitude')

    if not (cadastral_number and latitude and longitude):
        response = JSONResponse({'error': 'Absent content for processing'})
        response.status_code = 400
        return response

    query_id = str(uuid.uuid4())
    data = {
        'id': query_id,
        'cadastral_number': cadastral_number,
        'coordinats': (longitude, longitude)
    }

    global processing_results
    processing_resultats[query_id] = asyncio.create_task(imitation_send_query(data))
    return {'id': query_id}


@router.get('/{query_id}')
async def get_result(query_id):
    try:
        result = processing_resultats[query_id].result()
        return {'calculated': True}

    except KeyError:
        response = JSONResponse({'error': 'wrong id'})
        response.status_code = 404
        return response

    except asyncio.exceptions.InvalidStateError:
        return {'calculated': False}


