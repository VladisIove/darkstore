FROM python:3.9

RUN pip install --upgrade pip
ENV PATH=$HOME/.local/bin:$PATH

WORKDIR /var/app

COPY ./portfolio_manager/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./portfolio_manager /var/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]