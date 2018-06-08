from flask import Blueprint, request
from app.modules.acquisitions.acquisition_model import AcquisitionModel
from core.utils import create_json_response,handle_error
from core.ndb import ndb

from app.exceptions import (
    InvalidFormatException,
    InvalidQueryParamsException,
    ResourceNotFoundException
)

acquisitions = Blueprint('acquuisitions',__name__, url_prefix='/api/acquisitions')

@acquisitions.route('', methods=['POST'])
def create():
    try:
        req_body = request.get_json()

        {
            "name":  "Syd"
            "Last_na"
        }
        {publishers}

        properties = {key: value for key, value in req_body.iteritems()
                      if key in AcquisitionModel._properties}

        return create_json_response(AcquisitionModel(**properties).put().get())
    except Exception as error:
        handle_error(error)

@acquisitions.route('', methods=['GET'])
def get_all():
    try:
        req_args = request.args

        properties = {key: value for key, value in req_args.iteritems()
                      if key in AcquisitionModel._properties}
        properties['is_deleted'] = properties.get('is_deleted', False)
        query = AcquisitionModel.find_all_by_properties(**properties)

        page = req_args.get('page', None)
        size = req_args.get('size', 20 if page else None)
        sort = AcquisitionModel._properties[req_args.get('sort', 'created')]
        order = req_args.get('order', 'desc')

        query = query.order(sort if order == 'asc' else
                            -sort if order == 'desc' else None)

        return create_json_response({
            'data': (
                query.fetch(size, offset=((page - 1) * size)) if page else
                query.fetch(size) if size else
                query.fetch()
            ),
            'total_count': query.count()
        })
    except Exception as error:
        handle_error(error)

@acquisitions.route('/<string:url_safe>', methods=['GET'])
def get(url_safe):
    try:
        entity = ndb.Key(urlsafe=url_safe).get()

        if entity is None or entity.is_deleted:
            raise ResourceNotFoundException(
                "No entity with url-safe '{}' exist.".format(url_safe))

        return create_json_response(entity)

    except Exception as error:
        handle_error(error)



