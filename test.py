{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "test.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPw6Ml99iP2bYWryqGH7kdT"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 401
        },
        "id": "QRR84Peebw4m",
        "outputId": "31227753-02e3-47bb-8714-a45dd19c350f"
      },
      "source": [
        "import random\n",
        "def  quick(arr,low,high):\n",
        "  def partition(arr, low, high):\n",
        "    i = (low-1)\n",
        "    pivot = arr[high]\n",
        "    for j in range(low, high):\n",
        "      if arr[j] <= pivot:\n",
        "        i = i+1\n",
        "        arr[i], arr[j] = arr[j], arr[i]\n",
        "\n",
        "    arr[i+1], arr[high] = arr[high], arr[i+1]\n",
        "    return (i+1)\n",
        "  def quickSort(arr, low, high):\n",
        "    if len(arr) == 1:\n",
        "      return arr\n",
        "    if low < high:\n",
        "      pi = partition(arr, low, high)\n",
        "      quickSort(arr, low, pi-1)\n",
        "      quickSort(arr, pi+1, high)\n",
        "\n",
        "\n",
        "n = 0\n",
        "a = 0\n",
        "while n < 1000000:\n",
        "  n = n + 10000\n",
        "  while a <10000:\n",
        "    a = a+1\n",
        "    arr.append(random.randint(1,100000))\n",
        "    print(arr)\n",
        "n = len(arr)\n",
        "quick(arr, 0, n-1)\n",
        "print(\"Sorted array is:\")\n",
        "print(max(arr))\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "IOPub data rate exceeded.\n",
            "The notebook server will temporarily stop sending output\n",
            "to the client in order to avoid crashing it.\n",
            "To change this limit, set the config variable\n",
            "`--NotebookApp.iopub_data_rate_limit`.\n",
            "\n",
            "Current values:\n",
            "NotebookApp.iopub_data_rate_limit=1000000.0 (bytes/sec)\n",
            "NotebookApp.rate_limit_window=3.0 (secs)\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-18-48ff96ff9c1d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     27\u001b[0m     \u001b[0ma\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     28\u001b[0m     \u001b[0marr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrandom\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrandint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m100000\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 29\u001b[0;31m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     30\u001b[0m \u001b[0mn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     31\u001b[0m \u001b[0mquick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mn\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    }
  ]
}