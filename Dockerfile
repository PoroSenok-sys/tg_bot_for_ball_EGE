FROM python:3.12

RUN mkdir /tg_bot_for_ball_EGE

WORKDIR /tg_bot_for_ball_EGE

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD alembic upgrade head && gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
