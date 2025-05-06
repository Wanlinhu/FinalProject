<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Spend Bill Gates' Money</title>
  <style>
    body {
      font-family: sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
    }
    header {
      background-color: #4caf50;
      color: white;
      text-align: center;
      padding: 1rem;
    }
    .money {
      font-size: 2rem;
      text-align: center;
      margin: 2rem 0;
    }
    .items {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1rem;
      padding: 1rem;
      max-width: 1000px;
      margin: auto;
    }
    .item {
      background: white;
      padding: 1rem;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
      text-align: center;
    }
    .item img {
      width: 100%;
      max-height: 150px;
      object-fit: contain;
    }
    .item h3 {
      margin: 0.5rem 0;
    }
    .item button {
      padding: 0.5rem 1rem;
      background-color: #4caf50;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .item button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <header>
    <h1>Spend Bill Gates' Money</h1>
  </header>

  <div class="money" id="moneyDisplay">$100,000,000,000</div>

  <div class="items" id="itemContainer"></div>



