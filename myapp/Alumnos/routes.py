from flask import Blueprint

alum=Blueprint('alum',__name__)

@alum.route('/getalum', methods=['GET'])
def getalum():
    return {'key':'Alumnos'}