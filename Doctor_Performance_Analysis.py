{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "acbc664b-969d-444e-b601-585121f67a58",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "center1 = pd.read_csv(\"Ahmedabad.csv\")\n",
    "center2 = pd.read_csv(\"Mehsana.csv\")\n",
    "center3 = pd.read_csv(\"Patan.csv\")\n",
    "center4 = pd.read_csv(\"Palanpur.csv\")\n",
    "center5 = pd.read_csv(\"Himatnagar.csv\")\n",
    "center6 = pd.read_csv(\"Modasa.csv\")\n",
    "center7 = pd.read_csv(\"Jamnagar.csv\")\n",
    "center8 = pd.read_csv(\"Dwarka.csv\")\n",
    "center9 = pd.read_csv(\"Somnath.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "33ab6774-350c-4ee2-af36-5b8a1796f1b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "li = [\"Ahmedabad\",\"Mehsana\",\"Patan\",\"Palanpur\",\"Himatnagar\",\"Modasa\",\n",
    "     \"Jamnagar\",\"Dwarka\",\"Somnath\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6641c4b6-46cb-481a-a8e6-e6dffb643b90",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cleandata(df1 , center):\n",
    "    df1[\"dschg_dt\"] = pd.to_datetime(df1[\"dschg_dt\"], format=\"%d/%m/%Y\")\n",
    "    df1[\"adm_dt1\"] = pd.to_datetime(df1[\"adm_dt1\"], format=\"%d/%m/%Y\")\n",
    "    los = (df1[\"dschg_dt\"] - df1[\"adm_dt1\"]).dt.days\n",
    "    df1[\"LOS\"] = np.where(los == 0, 1, los)\n",
    "    \n",
    "    \n",
    "    df1[\"NetAmt\"] = (\n",
    "        df1[\"NetAmt\"]\n",
    "        .astype(str)\n",
    "        .str.replace(r\"[^\\d.-]\", \"\", regex=True)  \n",
    "    )\n",
    "    \n",
    "    df1[\"MedAmt_Cst\"] = (\n",
    "        df1[\"MedAmt_Cst\"]\n",
    "        .astype(str)\n",
    "        .str.replace(r\"[^\\d.-]\", \"\", regex=True)\n",
    "    )\n",
    "    df1[\"NetAmt\"] = pd.to_numeric(df1[\"NetAmt\"], errors=\"coerce\")\n",
    "    df1[\"MedAmt_Cst\"] = pd.to_numeric(df1[\"MedAmt_Cst\"], errors=\"coerce\")\n",
    "    df1[\"Profit\"] = df1[\"NetAmt\"] - df1[\"MedAmt_Cst\"]\n",
    "    \n",
    "    df1[\"Center\"] = center\n",
    "    \n",
    "    df1 = df1.drop([\"Textbox112\", \"Textbox27\", \"Textbox38\"], axis=1)\n",
    "    \n",
    "    col = df1.pop(\"LOS\")\n",
    "    df1.insert(6,\"LOS\",col)\n",
    "    \n",
    "    col = df1.pop(\"Profit\")\n",
    "    df1.insert(15,\"Profit\",col)\n",
    "\n",
    "    df1.columns = [\"Ptn_No\", \"IP_No\", \"Patient_Name\",\"Comp_Code\",\n",
    "                  \"Adm_Dt\",\"Dischrg_Date\",\"LOS\",\"Bill_No\",\"Bill_Date\",\"Doctor\",\"Class\",\n",
    "                  \"Bill_Amt\",\"Concession\",\"Net_Amt\",\"Cost_Value\",\"Profit\",\"MRP_Value\",\"User_ID\",\"Center_Name\"]\n",
    "    \n",
    "    return df1\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "30da1fbc-96cf-4ff2-9dc3-08e9319a031f",
   "metadata": {},
   "outputs": [],
   "source": [
    "ff1 = cleandata(center1,li[0])\n",
    "ff2 = cleandata(center2,li[1])\n",
    "ff3 = cleandata(center3,li[2])\n",
    "ff4 = cleandata(center4,li[3])\n",
    "ff5 = cleandata(center5,li[4])\n",
    "ff6 = cleandata(center6,li[5])\n",
    "ff7 = cleandata(center7,li[6])\n",
    "ff8 = cleandata(center8,li[7])\n",
    "ff9 = cleandata(center9,li[8])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "513736d6-7d3c-4c07-ac70-fbbc6c03a6ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_df = pd.concat([ff1, ff2, ff3, ff4,ff5,ff6,ff7,ff8,ff9], ignore_index=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fcb96e08-ae6f-4569-ac2c-4eaf844ccd4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "final_df.to_excel(\"output.xlsx\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f6a982a1-4579-4b65-969e-f8c670b377d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5016"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sqlalchemy import create_engine\n",
    "\n",
    "engine = create_engine(\"mysql+pymysql://root:password@localhost:3306/hosptal\")\n",
    "\n",
    "final_df.to_sql(\n",
    "    name=\"final_report\",\n",
    "    con=engine,\n",
    "    if_exists=\"replace\",\n",
    "    index=False\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2db0a0d7-bc0c-4dae-aa43-7ed44100caeb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
