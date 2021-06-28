import React from 'react';
import { Container, CssBaseline, Typography } from "@material-ui/core";
function App() {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="xl">
        <Typography
          component="div"
          style={{ backgroundColor: "#000", height: "100vh" }}
        />
      </Container>
    </React.Fragment>
  );
}

export default App;
