FROM node:17-buster-slim
WORKDIR /app
COPY . .

WORKDIR /app/client
COPY /client .
RUN npm install -g pnpm
RUN pnpm install
RUN pnpm build

FROM python:3.7-slim-buster
WORKDIR /app/server
COPY /server .
RUN pip3 install -r requirements.txt 
CMD [ "python3", "-m" , "uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]
