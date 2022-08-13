{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "e4bec97b-6330-4646-9743-d6044d44b030"
    },
    {
      "cell_type": "code",
      "source": "a = 2\na",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "67f8007a-e413-4c6d-90b7-ee939b851de7"
    },
    {
      "cell_type": "code",
      "source": "from flask import Flask, render_template, request",
      "metadata": {
        "trusted": true
      },
      "execution_count": 27,
      "outputs": [
        {
          "ename": "<class 'ModuleNotFoundError'>",
          "evalue": "No module named 'flask'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "Input \u001b[0;32mIn [27]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mflask\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Flask, render_template, request\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'flask'"
          ],
          "output_type": "error"
        }
      ],
      "id": "86a0140a"
    },
    {
      "cell_type": "code",
      "source": "app = Flask(__name__)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 28,
      "outputs": [
        {
          "ename": "<class 'NameError'>",
          "evalue": "name 'Flask' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "Input \u001b[0;32mIn [28]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0m app \u001b[38;5;241m=\u001b[39m \u001b[43mFlask\u001b[49m(\u001b[38;5;18m__name__\u001b[39m)\n",
            "\u001b[0;31mNameError\u001b[0m: name 'Flask' is not defined"
          ],
          "output_type": "error"
        }
      ],
      "id": "2c806a09"
    },
    {
      "cell_type": "code",
      "source": "import joblib\n\n@app.route(\"/\", methods=[\"GET\",\"POST\"])\ndef index():\n    if request.method == \"POST\":\n        rates = float(request.form.get(\"rates\"))\n        print(rates)\n        model1 = joblib.load(\"regression_DBS\")\n        r1 = model1.predict([[rates]])\n        model2 = joblib.load(\"tree_DBS\")\n        r2 = model2.predict([[rates]])\n        return(render_template(\"index.html\",result1=r1,result2=r2))\n    else:\n        return(render_template(\"index.html\",result1=\"waiting\",result2=\"waiting\"))",
      "metadata": {
        "trusted": true
      },
      "execution_count": 29,
      "outputs": [
        {
          "ename": "<class 'NameError'>",
          "evalue": "name 'app' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "Input \u001b[0;32mIn [29]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mjoblib\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;129m@app\u001b[39m\u001b[38;5;241m.\u001b[39mroute(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m/\u001b[39m\u001b[38;5;124m\"\u001b[39m, methods\u001b[38;5;241m=\u001b[39m[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGET\u001b[39m\u001b[38;5;124m\"\u001b[39m,\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPOST\u001b[39m\u001b[38;5;124m\"\u001b[39m])\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mindex\u001b[39m():\n\u001b[1;32m      5\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m request\u001b[38;5;241m.\u001b[39mmethod \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPOST\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[1;32m      6\u001b[0m         rates \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mfloat\u001b[39m(request\u001b[38;5;241m.\u001b[39mform\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrates\u001b[39m\u001b[38;5;124m\"\u001b[39m))\n",
            "\u001b[0;31mNameError\u001b[0m: name 'app' is not defined"
          ],
          "output_type": "error"
        }
      ],
      "id": "d1a4dae4"
    },
    {
      "cell_type": "code",
      "source": "if __name__ == \"__main__\":\n    app.run(host='localhost', port=5002, debug=False)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 30,
      "outputs": [
        {
          "ename": "<class 'NameError'>",
          "evalue": "name 'app' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "Input \u001b[0;32mIn [30]\u001b[0m, in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m----> 2\u001b[0m     \u001b[43mapp\u001b[49m\u001b[38;5;241m.\u001b[39mrun(host\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mlocalhost\u001b[39m\u001b[38;5;124m'\u001b[39m, port\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m5002\u001b[39m, debug\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m)\n",
            "\u001b[0;31mNameError\u001b[0m: name 'app' is not defined"
          ],
          "output_type": "error"
        }
      ],
      "id": "3e5ccf9e"
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "5e57ec78"
    }
  ]
}