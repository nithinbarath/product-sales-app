import axios from "axios";
import React, {useState} from "react";
import Add from "../img/addAvatar.png";
import { useNavigate,Link } from "react-router-dom";

const Register = ({baseUrls}) => {
    const navigate = useNavigate()

    const [registerData,setRegisterData] = useState({
        username:"",
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
        axios.post(`${baseUrls}/signup`,
        {
            username: registerData.username,
            email:registerData.email,
            password:registerData.password})
        .then(response => {
            // data.notes ="";
            console.log(response)
            // autoUpdate();
        })
        .catch(error => {
            console.log(error)
        })
    }
    return (
        <div className="formContainer">
            <div className="formWrapper">
                <span className="logo">Message App</span>
                <span className="title">Register</span>
                <form onSubmit={submitHandler}>
                    <input required 
                    type="text" 
                    name="username"
                    value={registerData.username}
                    onChange={changeHandler}
                    placeholder="display name"/>
                    <input required type="email" 
                    name="email"
                    value={registerData.email}
                    onChange={changeHandler}
                    placeholder="email"/>
                    <input type="password" 
                    name="password"
                    value={registerData.password}
                    onChange={changeHandler}
                    placeholder="password"/>
                    <input style={{display:"none"}} type="file" id="file"/>
                    <label htmlFor="file">
                        <img src={Add} alt="" />
                        <span>Add an avatar</span>
                    </label>
                    <button type="submit">Sign up</button>
                </form>
                <p>You do have an account? <Link to="/login">Login</Link></p>
            </div>
        </div>
    )
}

export default Register;