# config

## keycloak

Included are definitions of both a demo realm and a couple users that will be imported by the container startup.
Secrets are included in these files, so treat this as example configuration only.

```yaml
volumes:
      - ./config/keycloak/:/opt/keycloak/data/import
command: start-dev --import-realm
```

### Generating the configuration files

The realm file can be generated using the export function directly in the keycloak admin app.
The users file (and/or the realm file) can be generated via the `kc.sh` script in the container:

```sh
# Host:
podman stop keycloak
podman commit keycloak demo-export
podman run -it --name export --entrypoint sh demo-export:latest
# Container:
cd /opt/keycloak
./bin/kc.sh export --users same_file --realm demo --dir .
exit
# Host:
podman cp export:/opt/keycloak/demo-users-0.json config/keycloak
podman rm export
```

## oauth2-proxy

The proxy config is included here and contains the cookie secret and the oidc client secret for the keycloak demo realm.
Again, since secrets are included, treat this as example configuration only.
