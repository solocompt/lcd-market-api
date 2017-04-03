market-api:
  image: marketapi:development
  container_name: market-api
  hostname: api
  environment:
    - VIRTUAL_HOST=api.market.local
    - APP_IN_PRODUCTION=false
    - TERM=xterm
    - SECRET_KEY=ghfsdfsadkuychf3453rwer45zgfiruy65465df
    - DEBUG=True
    # If providing multiple servers use localhost:3000,api.local,api.example.com
    - CORS_ORIGIN_ALLOW_ALL=True
    - CORS_ORIGIN_WHITELIST=localhost:3000,localhost:8000,market.soloweb.pt,market.local
  expose:
    - "80"
    # port 22 only required for development purposes
    - "22"
  volumes:
    - ~/repos/market-api:/var/www
  links:
    - market-database
market-database:
  image: registry.soloweb.pt/postgres-database:latest
  container_name: market-database
  hostname: database
  environment:
    - TERM=xterm
  volumes:
    - /var/lib/postgresql/data
market-dbadmin:
  image: registry.soloweb.pt/postgres-dbadmin:latest
  container_name: market-dbadmin
  hostname: dbadmin
  environment:
    - VIRTUAL_HOST=dbadmin.market.local
    - TERM=xterm
  expose:
    - "80"
  links:
    - market-database
