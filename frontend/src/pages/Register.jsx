import React from "react";
import Add from "../img/addAvatar.png";
import { useNavigate,Link } from "react-router-dom";

const Register = () => {
    const navigate = useNavigate()
    return (
        <div className="formContainer">
            <div className="formWrapper">
                <span className="logo">Message App</span>
                <span className="title">Register</span>
                <form>
                    <input required type="text" placeholder="display name"/>
                    <input required type="email" placeholder="email"/>
                    <input type="password" placeholder="password"/>
                    <input style={{display:"none"}} type="file" id="file"/>
                    <label htmlFor="file">
                        <img src={Add} alt="" />
                        <span>Add an avatar</span>
                    </label>
                    <button>Sign up</button>
                </form>
                <p>You do have an account? <Link to="/login">Login</Link></p>
            </div>
        </div>
    )
}

export default Register;