import './App.css';
import "./style.scss";
import {
  createBrowserRouter,
  RouterProvider,
  Route,
  Link,
  BrowserRouter,
  Routes,
} from "react-router-dom";
import React, { useState } from "react";
import Register from './pages/Register';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';

function App() {
  const [baseUrl_d, setBaseUrl] = useState("http://localhost:9559/api")
  return (
   <BrowserRouter>
   <Routes>
    <Route path='/'>
      <Route index element={<Register baseUrls={baseUrl_d}
      />}/>
      <Route path='login' element={<Login baseUrls={baseUrl_d}
      />}/>
      <Route path='register' element={<Register baseUrls={baseUrl_d}
      />}/>
      <Route path='dashboard' element={<Dashboard baseUrls={baseUrl_d}
      />}/>
    </Route>
   </Routes>
   </BrowserRouter>
  );
}

export default App;
