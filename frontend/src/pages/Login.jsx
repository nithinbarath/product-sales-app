import React from "react";
import Add from "../img/addAvatar.png";
import { useNavigate,Link } from "react-router-dom";

const Login = () => {
    const navigate = useNavigate()
    const handleSubmit = () => {
        navigate("/register")
    }
    return (
        <div className="formContainer">
            <div className="formWrapper">
                <span className="logo">Message App</span>
                <span className="title">Register</span>
                <form onSubmit={handleSubmit}>
                    <input required type="email" placeholder="email"/>
                    <input type="password" placeholder="password"/>
                    <button>Login</button>
                </form>
                <p>You don't have an account?<Link to="/register">Register</Link></p>
            </div>
        </div>
    )
}

export default Login;