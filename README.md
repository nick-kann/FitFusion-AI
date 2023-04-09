
<h1> 💪 FitFusion AI 💪 </h1>

## 📝 Overview 📝
Fitfusion is an AI-powered fitness project that offers a personalized workout schedule and plan based on your characteristics. To enhance each workout, it provides a tracker that uses computer vision to ensure proper form and keeps a record of your workout results so you can track your progress over time. It also includes a personalized AI trainer to answer your fitness questions. Achieve your fitness goals with our cutting-edge technology.

## 🎬 Demo 🎬 



## ⚙️ How it Works ⚙️
FitFusion AI is an innovative fitness project that utilizes advanced AI and computer vision technology to help you achieve your fitness goals. The project comprises three main components: personalized workout plan, rep tracker, and personalized fitness trainer.

To create a personalized workout plan, our AI algorithm analyzes a combination of your inputted characteristics, such as weight, height, fitness level, and workout goals. Based on this analysis, the algorithm generates a customized workout plan tailored to your specific needs.

Once you select the workout you want to do, you can move onto our rep tracker. Our rep tracker utilizes OpenCV and MediaPipe Pose Landmark Estimation to track multiple body parts and analyze various distances and angles in three dimensions to ensure that you perform each rep with proper form. After each workout, the number of completed reps is stored and can be viewed in a graph displaying your progress over time.

Lastly, we include a personalized fitness trainer is powered by a customized version of GPT3.5-Turbo that is fine-tuned to provide expert advice on any fitness-related questions you may still have. Whether you need guidance on exercise techniques, nutrition, or workout routines, our AI trainer is there to help.

With our cutting-edge technology and personalized approach to fitness, FitFusion AI is the perfect tool to help you achieve your fitness goals.

## 🚀 Usage 🚀
<p> To run this project on your own you must do the following steps 
<br></br>
  <b>1.</b> Navigate to a command line and clone the repository 
</p>

```
git clone https://github.com/butter-my-toast/yelp-guru/ 
```
<p>
  <b>2.</b> Start the server and take note of the IP 
</p>

```
cd yelp-guru
python main.py
```
<p>
  The output should be something similar to the following code segment:
</p>

```
 * Serving Flask app 'main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.1.126.35:43/ (Press CTRL+C to quit)
```
<p>
  <b>3.</b> Then open a new terminal and navigate back into the yelp-guru directory and modify the HomePage.jsx file located at "pioneerHacksFrontEnd/pioneerHacksFrontEnd/src/components/Homepage/Homepage.jsx".
  Find the fetch function on line 29 and replace the URL with your server ip given in the previous command.
  Then navigate to the pioneerHacksFrontEnd/pionerHacksFrontEnd folder and run the following command:
</p>

```
npm install
npm run dev
```
<p>
  And with that, it should all be up and running!
</p>

## 🛠️ Technologies used 🛠️
  Front-end: <b>[React.js](https://github.com/facebook/react/blob/main/LICENSE)</b> \
  React is used for the entire webview of the project \
  \
  Back-end: <b>[Flask](https://github.com/pallets/flask/blob/main/LICENSE.rst "Flask license")</b> \
  Flask is used to connect our data processing to the front-end \
  \
  Inference API: <b>[Hugging Face](https://huggingface.co/ "Hugging Face")</b> \
  Hugging Face's Inference API was used to quickly access the NLP models without any cost \
  \
  Named-entity recognition: <b>[InstaFoodRoBERTa-NER](https://huggingface.co/Dizex/InstaFoodRoBERTa-NER "InstaFoodROBERTa-NER")</b> \
  Dizex's fine-tuned BERT model was used to recognize the food entities in our Yelp reviews \
  \
  Aspect-based sentiment analysis: <b>[deberta-v3-large-absa-v1.1](https://huggingface.co/yangheng/deberta-v3-large-absa-v1.1 "deberta-v3-large-absa-v1.1")</b> \
  Yangheng's ABSA model was used to determine the sentiment of a specific food in a review \
  \
  Food database: <b>[FoodData Central](https://fdc.nal.usda.gov/ "FoodData Central")</b> \
  The U.S. Department of Agriculture's food database was used to find the calories of foods and determine the health scores for them
  

## 🧑‍💻 Authors 🧑‍💻
Alexander S. Du / [@Mantlemoose](https://github.com/Mantlemoose "Mantlemoose's github page") \
Alex Y. Du / [@alexyd88](https://github.com/alexyd88 "alexyd88's github page") \
Eashan Chatterjee / [@EashanC23](https://github.com/EashanC23 "EashanC23's github page") \
Nicholas Kann / [@butter-my-toast](https://github.com/butter-my-toast "butter-my-toast's github page")
