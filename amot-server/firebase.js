const firebase = require('firebase')
// const firestore = require('firebase/app/firestore')

var firebaseConfig = {
    apiKey: "AIzaSyBKX2OfHmeEntaYPaMkbkd1n-I0Waaf-gI",
    authDomain: "asw-solution.firebaseapp.com",
    projectId: "asw-solution",
    storageBucket: "asw-solution.appspot.com",
    messagingSenderId: "797971068282",
    appId: "1:797971068282:web:2d0961eac69d8b7bfb92c3"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore()
const things = db.collection('things')
const components = db.collection('components')


module.exports = {
    things,
    components
}