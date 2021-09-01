from fastapi import APIRouter
from parser import get_info
import utils
import schemas

router = APIRouter()


@router.post('/account')
def log_inst(request: schemas.BaseAccount):
    utils.delete_config()
    return get_info(request.username)

