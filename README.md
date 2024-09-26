# feedback_service


в корне проекта и в папке <code>tg_bot</code>:<br>
переименовать <code>dotenv-example</code> в <code>.env</code> и исправить данные на актуальные<br>

далее <code>docker-compose up --build</code><br>
<code>docker ps</code> - копируем id контейнера feedback_service-app<br>
<code>docker exec -it <id_контейнера> python manage.py createsuperuser</code>

создание опроса - /form/
