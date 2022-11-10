## Command to use

```bash
docker build .

docker run --rm -v $(pwd):/code -e "JEKYLL_ENV=production" -it DOCKER_IMAGE jekyll build

firebase deploy
```