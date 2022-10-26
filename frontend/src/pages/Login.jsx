import axios from "axios";
import React,{useState} from "react";
import { useNavigate,Link } from "react-router-dom";

const Login = () => {
    const navigate = useNavigate()

    const [registerData,setRegisterData] = useState({
        email:"",
        password:""
    })

    const changeHandler = e =>{
        const newData={...registerData}
        newData[e.target.name] = e.target.value
        setRegisterData(newData)
        console.log("newData" + newData)
    }

    const submitHandler = e => {
        e.preventDefault()

        let bodyFormData = new FormData();
        bodyFormData.append('username', registerData.email);
        bodyFormData.append('password', registerData.password);
        const config = {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }

        axios.post("http://localhost:9559/api/login", bodyFormData, config).then(res => {
            if (res.status === 200){
           
                navigate("/register")
                axios.get("http://localhost:9559/api/verify")
                    .then(res => {
                        if(res.status === 200){
                            
                        }
                    })
                localStorage.setItem("auth", true);
            }else{
                console.log("Incorrect Details. Please try again.", 2000);
                alert("Please provide valid credentials");
            }
        }).catch(err => {
            console.log("Incorrect Details. Please try again.", 2000);

            if (err.response) {
                if(err.response.status !== 401 && err.response.status !== 200){
                    console.log("Incorrect Details. Please try again.", 2000);
                    alert("Please provide valid credentials");
                    // message.error(err.response.data.detail, 5);
                }
            }
        })
            .finally(() =>{
            });
    }
  
    return (
        <div className="formContainer">
            <div className="formWrapper">
                <span className="logo">Message App</span>
                <span className="title">Sign in</span>
                <form onSubmit={submitHandler}>
                    <input required type="text" 
                     name="email"
                     value={registerData.email}
                     onChange={changeHandler}
                     placeholder="email"/>
                    <input type="password" 
                     name="password"
                     value={registerData.password}
                     onChange={changeHandler}
                     placeholder="password"/>
                    <button type="submit">Login</button>
                </form>
                <p>You don't have an account?<Link to="/register">Register</Link></p>
            </div>
        </div>
    )
}

export default Login;