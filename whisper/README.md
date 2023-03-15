
## How to run the container?
1. Open a terminal and navigate to the folder where you created the files.
2. Run the following command to build the container:

```bash
docker build -t whisper-api .
```
3. Run the following command to run the container:

```bash
docker run -p 5000:5000 whisper-api
```

## How to test the API?
1. You can test the API by sending a POST request to the route `http://localhost:5000/whisper` with a file in it. Body should be form-data.
2. You can use the following curl command to test the API:

```bash
curl -F "file=@/path/to/file" http://localhost:5000/whisper
```
3. In result you should get a JSON object with the transcript in it.

## How to deploy the API?
This API can be deployed anywhere where Docker can be used. Just keep in mind that this setup currently using CPU for processing the audio files.
If you want to use GPU you need to change Dockerfile and share the GPU. I won't go into this deeper as this is an introduction.
[Docker GPU](https://docs.docker.com/config/containers/resource_constraints/)

You can find the whole code [here]()

**Thank you** for reading! If you enjoyed this tutorial you can find more and continue reading 
[on our tutorial page](https://lablab.ai/t/)

---

[![Artificial Intelligence Hackathons, tutorials and Boilerplates](https://storage.googleapis.com/lablab-static-eu/images/github/lablab-banner.jpg)](https://lablab.ai)

