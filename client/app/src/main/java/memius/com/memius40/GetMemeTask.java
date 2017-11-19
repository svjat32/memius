package memius.com.memius40;


import android.os.AsyncTask;
import android.widget.EditText;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import org.json.*;

import java.util.concurrent.ExecutionException;

/**
 * Created by lexay on 18.11.2017.
 */

class GetMemeTask extends AsyncTask<String, Void, JSONObject> {
    private  OnTaskCompleted listener;
    private Exception exception;

    public GetMemeTask ( OnTaskCompleted listener){
        this.listener = listener;
    }


    protected JSONObject doInBackground(String... urls) {

        try {

            String url = GlobalVars.url + "GetMeme.py";
            HttpResponse<String> response = Unirest.post(url)
                    .header("content-type", "application/x-www-form-urlencoded")
                    .body("SessionId=" + GlobalVars.sessionID + "&MemeId=" + "1")
                    .asString();
            String bodyString = response.getBody();
            JSONObject json = new JSONObject(bodyString);

            return json;
        }
        catch(Exception e) {
            System.out.println("Error: " + e.toString());
            return null;
        }
    }

    protected void onPostExecute(JSONObject feed) {
        try {
            listener.onTaskComleted();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}