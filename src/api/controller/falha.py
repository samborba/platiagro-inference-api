import json
import logging
import os
from flask import Blueprint, abort, request, jsonify, make_response

from utils import isolation_forest_inference, logistic_regression_inference
 
blueprint = Blueprint("predict", __name__)


@blueprint.route("/", methods=['POST'])
def home_page():
    data = request.json
    incoming_array = data['ndarray']
    nd_array = []

    for value in incoming_array:
        nd_array.append(float(value))
 
    rpm_value = nd_array.pop(); # pop RPM
    rpm_array = ["RPM", rpm_value]
    anomaly = isolation_forest_inference(nd_array)
    falha = logistic_regression_inference(anomaly, rpm_array)

    response = {'data': falha}

    # logging.info(response)

    return jsonify(response), 200
