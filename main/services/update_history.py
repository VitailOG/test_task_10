from django.utils.timezone import now


def update_hotel_history(history, meta_hotel):
    current_date = now().isoformat()
    if len(history['history']) > 0:
        if history['history'][-1]['id'] == meta_hotel.id:
            return history
        history['history'][-1]['leave'] = current_date

    data = {
        "id": meta_hotel.id,
        "name": meta_hotel.name,
        "join": current_date,
        "leave": None
    }
    history['history'].append(data)
    return history
