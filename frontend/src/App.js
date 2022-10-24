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
import Register from './pages/Register';
import Login from './pages/Login';

function App() {
  return (
   <BrowserRouter>
   <Routes>
    <Route path='/'>
      <Route index element={<Register/>}/>
      <Route path='login' element={<Login/>}/>
      <Route path='register' element={<Register/>}/>
    </Route>
   </Routes>
   </BrowserRouter>
  );
}

export default App;
