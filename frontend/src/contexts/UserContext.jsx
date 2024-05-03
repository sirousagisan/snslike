import { createContext, useReducer, useState, useEffect } from "react";
import axios from "axios"
import { useNavigate } from "react-router-dom";

const IsLoginContext = createContext()

const UserProvider = ({ children }) => {
  const [ isLogin, setIsLogin ] =  useState(false)
  const navigate = useNavigate()
  const checkAccessTokenValidity = () => {
    axios.get("http://127.0.0.1:8080/auth/islogin").then((res) => {
      setIsLogin(true)
      navigate("/")
    }).catch((res) => {
      console.log("Failed Login");
    })
  };

  // useEffect(() => {
  //   // コンポーネントがマウントされた時、およびisLoginの値が変更された時に実行される
  //   checkAccessTokenValidity();
  //   // 10分ごとにアクセストークンの有効性をチェックする
  //   const interval = setInterval(checkAccessTokenValidity, 10 * 60 * 1000);

  //   return () => clearInterval(interval);
  // }, [isLogin]);
  return (
    <IsLoginContext.Provider value={{isLogin, setIsLogin}}>
      { children }
    </IsLoginContext.Provider>
  )
}

export {UserProvider, IsLoginContext}
