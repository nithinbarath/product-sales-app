import axios from "axios";
import React, {useState, useEffect} from "react";
import { useNavigate} from "react-router-dom";



const Postlist = ({notesUpdate,setNotesUpdate, baseUrls}) => {
    const [data, setDAta] = useState({
        notes:"",
        posts:[],
        errorMsg:""
    })

    const autoUpdate = () => {
        axios.get(`${baseUrls}/list/todolist`)
        .then(response => {
            console.log(response)
            setDAta({posts:response.data})
        })
        .catch(error => {
            console.log(error)
            this.setDAta({errorMsg: 'Error retreiving data'})
        })

    }
    const changeHandler = e =>{
        const newData={...data}
        newData[e.target.name] = e.target.value
        setDAta(newData)
        console.log("newData" + newData)
    }
    const submitHandler = e => {
        e.preventDefault()
        axios.post(`${baseUrls}/create/todolist`,{notes: data.notes})
        .then(response => {
            data.notes ="";
            console.log(response)
            autoUpdate();
        })
        .catch(error => {
            console.log(error)
        })
    }
    useEffect(() => {
        autoUpdate();
    },[])

    const navigate = useNavigate()

    const UpdateHandle = (id,notes) => {
        const filters = data.posts.filter(obj => obj.id === id);
        console.log("id = "+ id)
        console.log("notes ="+ notes)
        console.log("filters = " + filters)
        console.log("posts = ")
        setNotesUpdate([id,notes]);
     
        navigate("/updatelist") 

    }

    const deleteHandle = (ids) => {
        console.log(ids)
      
        axios.delete(`${baseUrls}/delete/todolist`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            data: {
                "id" :  ids
            }
        })
        .then(response => {
            console.log(response)
            autoUpdate();
        })
        .catch(error => {
            console.log(error)
        })
    }

    return (
        <div  className="container">
            <div className="app-wrapper">
                <h1 className="header">Todo list</h1>
            <form onSubmit={submitHandler}>
                <div>
                <input 
                className="list-input"
                   type="text"
                   name="notes" 
                   value={data.notes}
                   onChange={changeHandler}
                   >
                   </input>
                
                <button type="submit" className="submit complete">Submit</button>
                </div>
            </form>

            <div>
                <div className="header">
                <h1>List of posts</h1>
                </div>
               
                {
                    data.posts.length ?
                    data.posts.map(post => 
                    <div key={post.id} className="list-item">
                        <p className="list">{post.notes}</p>
                        <button onClick={()=>UpdateHandle(post.id,post.notes)} className="button-complete"><i className="fa fa-check-circle"/> </button>
                        <button onClick={()=>UpdateHandle(post.id,post.notes)} className="button-edit"><i className="fa fa-edit"/> </button>
                        <button onClick={()=>deleteHandle(post.id)} className="button-delete task-button"><i className="fa fa-trash"/></button>
                    </div>):
                    null
                }
                {data.errorMsg ? <div>{data.errorMsg}</div> : null}
                
             </div>
             </div>
        </div>
    )
};

export default Postlist;