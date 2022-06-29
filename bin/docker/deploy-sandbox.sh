#!/bin/sh
# Seed builder
# AUTO_GENERATED (Read only)

KEY=$1
HOST=$2
GIT_URL=$3
GIT_BRANCH=$4
CLIENT_PORT=$(python -c "print($KEY + 0)")
DJANGO_PORT=$(python -c "print($KEY + 1)")
POSTGRES_PORT=$(python -c "print($KEY + 2)")
REDIS_PORT=$(python -c "print($KEY + 3)")
SERVER_URL="http://$HOST:$DJANGO_PORT"
CLIENT_URL="http://$HOST:$CLIENT_PORT"

chmod 400 .dev.pem
echo "== Updating project"
ssh -t -i .dev.pem "ubuntu@$HOST" "git clone $GIT_URL $KEY/api"
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;git reset --hard"
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;git clean -f -d"
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;git checkout $GIT_BRANCH"
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;git pull"

echo "== Configuring docker"
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sed -i \"s/run numeral_roman_django/run numeral_roman_django_$KEY/\" \"bin/setup.sh\""
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sed -i \"s/exec numeral_roman_django/exec numeral_roman_django_$KEY/\" \"bin/setup.sh\""
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sed -i \"s/numeral_roman_django/numeral_roman_django_$KEY/\" \"bin/docker/docker-compose.yml\""
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sed -i \"s/numeral_roman_postgres/numeral_roman_postgres_$KEY/\" \"bin/docker/docker-compose.yml\""
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sed -i \"s/numeral_roman_redis/numeral_roman_redis_$KEY/\" \"bin/docker/docker-compose.yml\""
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sed -i \"s/DB_HOST=numeral_roman_postgres/DB_HOST=numeral_roman_postgres_$KEY/\" \"bin/docker/env-dev.sh\""
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sed -i \"s/REDIS_HOST=numeral_roman_redis/REDIS_HOST=numeral_roman_redis_$KEY/\" \"bin/docker/env-dev.sh\""

echo "== Updating django server"
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sudo bin/setup.sh $DJANGO_PORT $POSTGRES_PORT $REDIS_PORT $SERVER_URL $CLIENT_URL"
ssh -t -i .dev.pem "ubuntu@$HOST" "cd $KEY/api;sudo bin/start.sh"

echo ""
echo "== Deployment completed (http://$HOST:$DJANGO_PORT)"
echo ""