var loggedIn = firebase.auth().currentUser;
	
var loginCheck = function() {
	var loggedIn = firebase.auth().currentUser;
	
	if(!loggedIn){
		alert("You are not logged in. Please sign in to access the firechat.");
	}
}

var styleObserver = new MutationObserver(loginCheck);
	
var hold = document.getElementById("loggedIn");

styleObserver.observe(hold, { attributes : true, attributeFilter : ['style'] });

firebase.auth().onAuthStateChanged(function(user) {
	  if (user) {
		this.actor = user;
		var displayName = document.getElementById("displayName").value;
		
		if(!user.displayName){
			user.updateProfile({
				displayName: displayName,
			})
		}
		if(!user.photoURL){
			user.updateProfile({
				photoURL: "profile-blank.png"
			})
				
		var newUser = {name:user.displayName,email:user.email,photoURL: user.photoURL}
		userRef.push().set(newUser);
		Proceed();
		
		// User is signed in.
		//console.log(user);
		
	  } 
	  else {
		// No user is signed in.
		console.log("no one arrived yet");
	  }
	}
});