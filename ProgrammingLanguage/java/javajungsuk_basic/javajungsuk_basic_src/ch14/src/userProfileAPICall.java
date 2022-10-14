import java.io.*;
import java.net.*;

// 계정 API 예제 사용자 정보 조회
public void userProfileAPICall(String accessToken) {  
    StringBuffer sb;
    String responseData = "";
    try{
        String apiURL = "https://prd.kr-ccapi.hyundai.com/api/v1/user/profile";
        URL url = new URL(apiURL);

        HttpURLConnection con = (HttpURLConnection)url.openConnection();

        con.setRequestMethod("GET");

        // Set Header Info
        con.setRequestProperty("Authorization", "Bearer " + accessToken);

        int responseCode = con.getResponseCode();
        BufferedReader br;
        if(con.getResponseCode() == HttpURLConnection.HTTP_OK){
            br = new BufferedReader(new InputStreamReader(con.getInputStream())); // 정상호출
        } else {
            br = new BufferedReader(new InputStreamReader(con.getErrorStream())); // 에러발생
        }

        sb = new StringBuffer();
        while ((responseData = br.readLine()) != null){
            sb.append(responseData);
        }
        br.close();

        System.out.println("responseCode = " + responseCode);
        System.out.println("userData = "+sb.toString());

    } catch (Exception e) {
        System.out.println(e);
    }
}

public static void main(String[] args) {
    userProfileAPICall user = new userProfileAPICall("0c0f92e7-e664-4677-bec1-5205b369bf9d");

}