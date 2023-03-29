from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_src():
    return "src app created!"
