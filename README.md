# front-end

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

### Replace files

Replace the files in the new project and delete the remaining files from the project initialization as such:

Replace/Add:

./my-vue-app/public/favicon.png
./my-vue-app/index.html
./my-vue-app/src/router.js
./my-vue-app/src/main.js
./my-vue-app/src/App.vue
./my-vue-app/src/components/HomePage.vue
./my-vue-app/src/components/TaxFormPage.vue

Delete:

./my-vue-app/src/components/HelloWorld.vue
./my-vue-app/src/assets/vue.svg
./my-vue-app/public/vite.svg
./my-vue-app/src/style.css
./my-vue-app/src/router/\*

### Install additional libraries

Run the following commands to install some necessary libraries:

```sh
npm install vue-router@4
```

```sh
npm install axios
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

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

## back-end

This part should help you understand how the backend API endpoints work.

There are two API endpoints, the cal_tax inside TaxCalculator and advgenerator inside openAIAdvisor.
The API endpoints are: '/calculate-tax' and '/tax-advice' respectively and the base URL is 'http://localhost:5000'.
HTTP requests with attached JSON data are sent to either one of those two endpoints.
To establish a valid communication, the base URL and one of the endpoint are combined into one URL, which is where the server expects to receive data.

## Tax calculator docs

In the case of the /calculate-tax endpoint, the server expects tax information and numbers.
Inside the API the server will use a formula to calculate the tax every time.
The greek taxing system is used in this case as the formula.
The useful information is then returned back to the frontend in the form of JSON.
This information includes: Total Income, Deductions, Taxable Income, Tax, Tax Credit, Total Tax, Tax Withheld and Net Tax.

## AI advisor docs for taxes

In the case of the /tax-advice endpoint, the server expects again tax information and numbers, together with possible comments the user might have added.
The data is manipulated and transformed so that it becomes a string input, which is then passed to the openai model.
For the integration of the AI model, the library openai is used.
A provided key is used to access the openai LLM (key is stored in another txt file for safety).
To establish connection with the AI model, a response chat-client is created through openai library, which takes multiple variables to help create the desired results.
Among these variables is the option for the model to have predefined characteristics, in this case to be an "AI tax advisor".
The user's request for advice is sent to the AI model and a generated answer is returned in the form of JSON.
The desired text is extracted and returned to the frontend.
