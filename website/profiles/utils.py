import uuid
def generate_refferal_code():
    code = str(uuid.uuid4()).replace("-","")[:12]
    return code
