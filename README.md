# Front-end

This template should help get you started developing with Vue 3 in Vite.
Make sure you have installed npm and Node.js in your machine.
You can install the latest version from: https://nodejs.org/ (npm comes with Node.js).

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Create new Vue.js project with Vite

```sh
npm init vite@latest my-vue-app --template vue
```

Replace my-vue-app with the desirable project name for the app.
Follow prompt's instructions and choose the options that best fit you (for this project choose Framework: Vue and Variant: JavaScript).

After that follow prompt's command suggestions:

```sh
cd my-vue-app
```

## Project Setup

```sh
npm install
```

## Replace files

Replace the files in the new project and delete the remaining files from the project initialization as such:

### Replace/Add:

./my-vue-app/public/favicon.png <br>
./my-vue-app/index.html <br>
./my-vue-app/src/router.js <br>
./my-vue-app/src/main.js <br>
./my-vue-app/src/App.vue <br>
./my-vue-app/src/components/HomePage.vue <br>
./my-vue-app/src/components/TaxFormPage.vue <br>

### Delete:

./my-vue-app/src/components/HelloWorld.vue <br>
./my-vue-app/src/assets/vue.svg <br>
./my-vue-app/public/vite.svg <br>
./my-vue-app/src/style.css <br>
./my-vue-app/src/router/\* <br>

## Brief Overview of the files for the front-end

**main.js** uses **App.vue** to initialize the app.<br>
**router.js** is used in the main to define the routes (URLs) for the two pages of our app.<br>
**styles.css** is used to define global styles in the App.<br>
Lastly the code for the two pages of the app is in the **HomePage.vue** and **TaxFormPage.vue**.<br>

## Install additional libraries

Run the following commands to install some necessary libraries:

```sh
npm install vue-router@4
```

```sh
npm install axios
```

## Compile and Hot-Reload for Development

```sh
npm run dev
```

## Compile and Minify for Production

This should build the frontend page in the folder /dist.

```sh
npm run build
```

From there you can run it by simply navigating to the /dist folder and running serve.

To install serve locally, run:

```sh
npm install serve --save-dev
```

Then run the following, in the dist folder, to run the page app:

```sh
npx serve
```

To install globally, run:

```sh
npm install --global serve
```

Then run in the dist folder:

```sh
serve
```

# Back-end

This part should help you understand how the backend API endpoints work.

The backend was developed using Python. For the APIs Flask RESTful was used as well as OpenAI for the AI model integration in one of the APIs.
There are two API endpoints, the cal_tax inside TaxCalculator and advgenerator inside OpenAIAdvisor classes, both of which are located in the routes.py file.
The API endpoints are: '/calculate-tax' and '/tax-advice' respectively and the base URL is 'http://localhost:5000'.
HTTP requests with attached JSON data are sent to either one of those two endpoints.
Communication is established through the combination of the base URL and one of the endpoints into one URL, which is where the server expects to receive data.

## Brief Overview of the files for the front-end

**init.py**: Responsible for initializing the Flask app and extensions.<br>
**routes.py**: Defines routes and attaches resources.<br>
**parsers.py**: Handles request parsing logic.<br>
**models.py**: Defines response models for marshaling.<br>
**tax_calculator.py**: Contains the core tax calculation logic.<br>
**utils.py**: Utility functions for shared tasks.<br>
**main.py**: application entry point.<br>
**requirements.txt**: library/framework dependencies.<br>

## Tax calculator docs

In the case of the /calculate-tax endpoint, the server expects tax information and numbers.
Inside the API, the server will use a formula to calculate the tax every time.
The greek taxing system is used in this case as the formula.
The useful information is then returned back to the frontend in JSON format.
This information includes: Total Income, Deductions, Taxable Income, Gross Tax, Tax Withheld, Tax Credit, and Net Tax Due.

## AI advisor docs for taxes

In the case of the /tax-advice endpoint, the server expects again tax information and numbers, together with possible comments the user might have added.
The data is manipulated and transformed so that it becomes a string input, which is then passed to the openai client model.
A key is needed to access the openai LLM. For safety reasons, the key is passed through an environment variable which will temporary save it for the current cmd prompt session.
To define the key as a temporary environment variable you run:<br>

For cmd:

```sh
set OPENAI_API_KEY=your_openai_key_here
```

For PowerShell:

```sh
$env:OPENAI_API_KEY = "your_openai_key_here"
```

To establish connection with the AI model, a response chat-client is created through openai library, which takes multiple variables to help create the desired results.
Among these variables is the option for the model to have predefined characteristics, in this case to be an "AI tax advisor".
The user's request for advice is sent to the AI model and a generated answer is returned in JSON format.
The desired text is extracted and returned to the frontend.

# Dockerization

For the dockerization of both frontend and backend we need docker. For windows Docker Desktop can be downloaded at https://www.docker.com/products/docker-desktop/.

## Separate build and run

To separately build and run the dockerfiles simply navigate to either **front-end** or **back-end** and run the following commands:

### Frontend

```sh
docker build -f Dockerfile_frontend -t deloitte-app-frontend-image .
```

```sh
docker run -p 8000:8000 deloitte-app-frontend-image
```

### Backend

```sh
docker build -f Dockerfile_backend -t deloitte-app-backend-image .
```

```sh
docker run -p 5000:5000 --env OPENAI_API_KEY deloitte-app-backend-image
```

## Simultaneous build and run

To build and run the two dockerfiles at the same time with out having to do each one separately, you can navigate where the docker-compose.yml file is and run:

```sh
docker-compose build
```

```sh
docker-compose up
```

Before running the backend, always remember to define the openai key as an environment variable.

# DevOps CI/CD with GitHub Actions

In order to create a CI pipeline with GitHub Actions, for automated testing create a directory at **.github/workflows**  
in there create a YAML file **ci.yml**. This file will create a pipeline that automatically executes a given testing file,
on every push that's performed to the main branch of the repository.
To the YAML file is defined, (similarly to docker): the files that will be tested, the libraries/framework that are used to run the app, as well as
the main languages that the frontend and the backend were developed with.
Two separate testing files were made for both the frontend and backend: **frontend_test.specs.js** and **backend_test.py**.
After the testing is complete, if all tests are successful, the defined files will be sent to a remote server through ssh connection.
There, any running process of older version of those files (if exist) is stopped and the old files are replaced. Finally the newer version files
are executed. All of these are performed in a maner that is also defined in the YAML file (e.g. docker-compose down/up).

## Front-end

The setup for the frontend test file required installing the following libraries:

```sh
npm install @testing-library/vue vitest @testing-library/jest-dom jsdom --save-dev
```

Next create a directory at **./front-end/test/** and there create a file **setup.js**.
In that file add: import `"@testing-library/jest-dom";`.
In **vite.config.js** add in the **defineConfig** function:

    `test: {`<br>
        `globals: true,`<br>
        `environment: "jsdom",`<br>
        `setupFiles: "./test/setup.js", // Add this line`<br>
    `},`<br>

Lastly add in the **package.json** file in the **scripts** the following line:
`"test": "vitest"`

Now you can run the **frontend_test.spec.js** code with the command (for development phase):

```sh
npm run test
```

## Back-end

The backend setup is simpler and faster. Install to your virtual environment the library pytest:

```sh
pip install pytest
```

now you can run the **backend_test.py** code.

## Automated testing with CI pipeline

    With
