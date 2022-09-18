import { useEffect } from "react";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";

const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <div className="container text-center">
        <h1>This is Home page</h1>
      </div>
    </>
  );
};

export default Home;
