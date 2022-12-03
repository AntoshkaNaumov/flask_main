from flask.views import MethodView
from flask import jsonify, request
from database import AdvertisementModel, OwnerModel, Session
from errors import ApiException
from validate import validate, CreateAdvertisementSchema, CreateOwnerSchema


class OwnerView(MethodView):

    def get(self, owner_id: int):
        with Session() as session:
            owner = session.query(OwnerModel).get(owner_id)
            if owner is None:
                raise ApiException(404, 'owner not found')

            return jsonify({
                'id': owner.id,
                'email': owner.email
            })


    def post(self):
        owner_data = validate(request.json, CreateOwnerSchema)
        with Session() as session:
            new_owner = OwnerModel(**owner_data)
            session.add(new_owner)
            session.commit()
            return jsonify({
                'id': new_owner.id,
                'email': new_owner.email
            })

    def patch(self, owner_id: int):
        owner_data = request.json
        with Session() as session:
            owner = session.query(OwnerModel).get(owner_id)
            for field, value in owner_data.items():
                setattr(owner, field, value)
            session.add(owner)
            session.commit()
            return jsonify({
                'id': owner.id,
                'email': owner.email
            })

    def delete(self, owner_id: int):
        with Session() as session:
            owner = session.query(OwnerModel).get(owner_id)
            session.delete(owner)
            session.commit()
            return jsonify({'status': 'deleted'})


class AdvertisementView(MethodView):

    def get(self, advertisement_id: int):
        with Session() as session:
            advertisement = session.query(AdvertisementModel).get(advertisement_id)
            if advertisement is None:
                raise ApiException(404, 'advertisement not found')

            return jsonify({'id': advertisement.id,
                            'title': advertisement.title,
                            'description': advertisement.description,
                            'owner_id': advertisement.owner_id
                            })


    def post(self):
        advertisement_data = validate(request.json, CreateAdvertisementSchema)
        with Session() as session:
            new_advertisement = AdvertisementModel(**advertisement_data)
            session.add(new_advertisement)
            session.commit()
            return jsonify({'id': new_advertisement.id,
                            'title': new_advertisement.title,
                            'description': new_advertisement.description,
                            'user_id': new_advertisement.owner_id
                            })


    def patch(self, advertisement_id: int):
        advertisement_data = request.json
        with Session() as session:
            advertisement = session.query(AdvertisementModel).get(advertisement_id)
            for field, value in advertisement_data.items():
                setattr(advertisement, field, value)
            session.add(advertisement)
            session.commit()
            return jsonify({'id': advertisement.id,
                            'title': advertisement.title,
                            'description': advertisement.description,
                            'owner_id': advertisement.owner_id
                            })


    def delete(self, advertisement_id: int):
        with Session() as session:
            advertisement = session.query(AdvertisementModel).get(advertisement_id)
            session.delete(advertisement)
            session.commit()
            return jsonify({'status': 'deleted'})

