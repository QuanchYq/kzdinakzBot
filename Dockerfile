FROM python:3.9
WORKDIR /app


# Install dependencies
COPY images /app/images
COPY courses.json /app/courses.json
COPY requirements.txt /app/requirements.txt
COPY keyboards.py /app/keyboards.py
COPY KosmeticsBot.py /app/KosmeticsBot.py
COPY libs.py /app/libs.py
COPY users.db /app/users.db
COPY usersname.db /app/usersname.db

RUN pip install -r requirements.txt



# Run the app
CMD ["python", "KosmeticsBot.py"]
