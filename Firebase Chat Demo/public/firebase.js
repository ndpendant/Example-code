var messageRef = firebase.database().ref("messages");
var userRef = firebase.database().ref("user");

this.messages = [];
this.users = [];
this.currentUser;

messageRef.on("child_added", snapshot => {
	this.messages.push(
	{
		date: snapshot.child("date").val(),
		message: snapshot.child("message").val(),
		user: snapshot.child("user").val(),
		photoURL: snapshot.child("photoURL").val()
	});
	
	riot.update();
});

userRef.on("child_added", snapshot => {
		var user = {	
						name:snapshot.child("name").val(),
						email: snapshot.child("email").val(),
						photoURL: snapshot.child("photoURL").val() 
					}
		
		var checkit = this.users.findIndex(i => i.email == user.email);
		
		if(checkit >= 0)
		{
			userRef.child(snapshot.key).remove();
		}
		else{
			this.users.push(user);
		}
		
		riot.update();
	});


function existToNewUser(){
	var exist = document.getElementById("existingUser");
	var newUser = document.getElementById("newUser");
	
	exist.style.display = "none";
	newUser.style.display = "block";
	
}

function newToExistingUser(){
	var exist = document.getElementById("existingUser");
	var newUser = document.getElementById("newUser");
	
	newUser.style.display = "none";
	exist.style.display = "block";
	
}

function Login(existing){
	if(existing == 1){
		var email = document.getElementById("existEmail").value;
		var password = document.getElementById("existPassword").value;
		
		firebase.auth().signInWithEmailAndPassword(email, password)
			.catch(function(error){ alert(error.message);});
	}
	else{
		var email = document.getElementById("newEmail").value;
		var password = document.getElementById("newPassword").value;
		var displayName = document.getElementById("displayName").value;
		
		if(displayName.length > 1){
		firebase.auth().createUserWithEmailAndPassword(email, password)
			.catch(function(error){ alert(error.message);});
		}
		else{
			alert("displayName must be provided.");
		}
	}
}

function Proceed(){
	var exist = document.getElementById("existingUser");
	var newUser = document.getElementById("newUser");
	var access = document.getElementById("loggedIn");
	
	newUser.style.display = "none";
	exist.style.display = "none";
	access.style.display = "block";
}


function duplicate(){
	var user = firebase.auth().currentUser;
	
	if(user){
		this.currentUser = {name: user.displayName,email: user.email,photoURL: user.photoURL}
	}
	for(var i = 0; i < this.users.length; i++)
	{
		if(this.users[i] == this.currentUser)
		{
			return true;
		}
	}
	return false;
};

function LogOut(){
	firebase.auth().signOut()
		.then(function(){
			
			var exist = document.getElementById("existingUser");
			var newUser = document.getElementById("newUser");
			var access = document.getElementById("loggedIn");
			
			newUser.style.display = "none";
			exist.style.display = "block";
			access.style.display = "none";
		});
}


function save(){
		var user = firebase.auth().currentUser;
		var MessageText = document.getElementById("msg").value;
		
		if(MessageText.length > 0){
		
			var newMessage = {date: new Date().toString(), message: MessageText, user: user.displayName, photoURL: user.photoURL };		
		
			messageRef.push().set(newMessage);
		
			riot.update();
			
			scrollDown.scrollTop = scrollDown.scrollHeight;

		}
		
		else{
			alert("No message provided");
		}
	};

riot.mount('mychat');
riot.mount('profileSetting');
