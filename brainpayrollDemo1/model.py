from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers.string import StrOutputParser
import os
import requests
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify



if __name__ == "__main__":
    #load_dotenv()
    print("Hello LangChain")    
    #print(os.environ["OPENAI_API_KEY"])
    prompt=open("website_text.txt","r").read()
    
    summary_template = prompt+"""You are payroll management company operating in UK.Your expertise is exclusively in Bulk Payroll Processing Engine
    Bulk Payroll Processing Engine,Statutory Automation,White Labelled portal,Payroll Grouping,Cloud Infrastructure,Auto Enrolment
    Real-time Reporting to HMRC,Holiday Pay Calculations,HR Management,payroll management,GDPR Compliance.if
    a question is not about brain payroll respond with ,"i can't assist with that,sorry!"
    Question:{information}
    Answer:
                        """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
    #llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    llm=ChatOllama(model="llama3",locals=True)

    chain = summary_prompt_template | llm | StrOutputParser()
    
    def query_llm(information):
        response=chain.invoke({'information':information})
        return response
        

    # while True:
    #     query_llm(input("please ask your question:- "))

    app=Flask(__name__)
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/chatbot",methods=["POST"])
    def chatbot():
        data=request.get_json()
        question=data["question"]
        response=query_llm(question)
        print(response)
        return jsonify({"response":response})
    if __name__=="__main__":
        app.run(debug=True)
