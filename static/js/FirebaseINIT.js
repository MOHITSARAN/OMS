
//Web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyAkQgPQdSHC1bEXvyoK0WMQKUIrJdKsiGc",
    authDomain: "androiddevelopment-983a0.firebaseapp.com",
    databaseURL: "https://androiddevelopment-983a0.firebaseio.com",
    projectId: "androiddevelopment-983a0",
    storageBucket: "androiddevelopment-983a0.appspot.com",
    messagingSenderId: "727541494286",
    appId: "1:727541494286:web:8bcb3f5b59e36e7b"
};
//Initialize Firebase
var FireBaseProject = firebase.initializeApp(firebaseConfig);
var defaultStorage = firebase.storage();