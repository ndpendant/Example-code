<mychat>
	<div class = "chat">
		<p each={i in messages}>
			<img src="{i.photoURL}" />
			<h>
				{i.date}
				<br/>
				<br/>
				<b>{i.user}</b>
				<br/>
				<br/>
				{i.message}
			</h>
			<br/>
		</p>	
	</div>

	<style>
		p {
			display: inline-block;
			padding-top: 15px;
			border-top: 3px #EAEBE8 solid;
			border-width: 1px;
			width: 100%;
		}
		
		h {
			display: inline-block;
			width: 700px;
		}
		
		img {
			display: inline-block; 
			width: 55px; 
			height: 55px;
			padding-right: 30px;
		}
		
	</style>
</mychat>

<profileSetting>
	<div class = "setting">
		<p>
			<img data-ref="imgPic" src="{pic}" />
			<h3>
				<b data-ref="un">{username}</b>	
				<br/>
				<br/>
				<a href="javascript:void(0)" onclick="LogOut()">Sign Out </a>
			</h3>
		</p>
	</div>
	
	<script>
		this.username = "test";
		this.pic = "profile_blank.png";
	
		firebase.auth().onAuthStateChanged(function(user) {
		});
		
		this.on('updated', function(){
			var user = firebase.auth().currentUser;
			
			if(user){
				this.refs.imgPic.src = user.photoURL;
				this.refs.un.textContent = user.displayName;
			}
			
		});
		
	</script>
	<style>
		img {
			display: inline-block; 
			width: 55px; 
			height: 55px;
			padding-right: 30px;
			padding-top: 10px; 
		}
		
		b{
			color:white;
		}
		
		h3{
			width: 60%;
			display: inline-block;
		}
		
		p{
			display: inline-block;
			width: 40%;
		}
		a{
			color:white;
		}
	</style>
</profileSetting>




