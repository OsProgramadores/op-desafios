<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Números Primos</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="container">
        <div class="header">
            <div class="social-network">
                <nav class="menu-nagation">
                    <ul>
                        <li>
                            <a href="https://github.com/weslley19">GITHUB</a>
                        </li>
                        <li>
                            <a href="https://instagram.com/weslley_oliveira19">INSTAGRAM</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="content">
            <div class="content-title">
                <header>
                    <h1>Números Primos</h1>
                </header>
            </div>

            <?php
                for ($i = 1; $i <= 10000; $i++)
                {
                    $divider = 0;

                    for ($j = $i; $j >= 1; $j--)
                    {
                        if ($i % $j == 0) {
                            $divider++;
                        }
                    }

                    if ($divider == 2) {
                        echo $i . " | ";
                    }
                }
            ?>

        </div>
    </div>
    
    <footer>
        <div class="button-action">
            <a href="index.html">VOLTAR</a>
        </div>
    </footer>

</body>
</html>