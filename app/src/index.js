import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle";
import "./index.css";

import Layout from "./Layout";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Layout />);
