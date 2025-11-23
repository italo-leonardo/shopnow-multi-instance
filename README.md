# ShopNow Multi-Instance — Load Balancing com Docker + Flask + NGINX

Este projeto demonstra como escalar uma aplicação web simples utilizando múltiplas instâncias Flask atrás de um balanceador de carga NGINX, tudo orquestrado com Docker Compose.

A arquitetura implementa:

3 instâncias independentes do serviço (APP-1, APP-2, APP-3)

Balanceamento de carga via NGINX (Round-Robin)

Detecção de falhas: se uma instância cair, o NGINX redireciona automaticamente o tráfego

Testes com Apache Benchmark (ab) para simular alta carga e concorrência

               ┌────────────────────┐
               │     Usuários        │
               └─────────┬──────────┘
                         │ 8080
               ┌─────────▼──────────┐
               │     NGINX LB        │
               │  (Load Balancer)    │
               └───────┬────┬───────┘
                       │    │
       ┌───────────────┘    └───────────────┐
 ┌─────▼─────┐    ┌──────▼─────┐     ┌──────▼─────┐
 │  APP-1     │    │  APP-2      │     │  APP-3      │
 │ Flask 5000 │    │ Flask 5000  │     │ Flask 5000  │
 └────────────┘    └─────────────┘     └─────────────┘

Como executar

1️Subir os containers
docker compose up -d --build

2️Testar no navegador:

Acesse:

http://localhost:8080

A cada atualização, você verá:

{"hostname": "31d6424eee95", "instance_id": "APP-2", "message": "ShopNow - OK"}