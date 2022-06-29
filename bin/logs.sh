#!/bin/bash
# Seed builder
# AUTO_GENERATED (Read only)

sudo docker-compose -f bin/docker/docker-compose.yml logs --follow --tail 250 numeral_roman_django numeral_roman_celery